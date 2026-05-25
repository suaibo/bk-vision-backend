# -*- coding: utf-8 -*-
import logging

from django.db.models import F
from django.utils.deprecation import MiddlewareMixin

from home_application.models import ApiAccessLog, ApiRequestCount


logger = logging.getLogger(__name__)

CMDB_BEHAVIORS = [
    "biz-list",
    "set-list",
    "module-list",
    "host-list",
    "host-detail",
]

JOB_BEHAVIORS = [
    "search-file",
    "backup-file",
    "backup-record",
]


class RecordUserBehaviorMiddleware(MiddlewareMixin):
    """Record selected API usage for BKVision analysis."""

    def process_request(self, request):
        try:
            api_name = request.path.rstrip("/").split("/")[-1]
            if api_name in CMDB_BEHAVIORS:
                api_category = "CMDB"
            elif api_name in JOB_BEHAVIORS:
                api_category = "JOB"
            else:
                return None

            api_request_count, _ = ApiRequestCount.objects.get_or_create(
                api_category=api_category,
                api_name=api_name,
            )
            api_request_count.request_count = F("request_count") + 1
            api_request_count.save(update_fields=["request_count"])
            user = getattr(request, "user", None)
            username = getattr(user, "username", "") or ""
            ApiAccessLog.objects.create(
                api_category=api_category,
                api_name=api_name,
                request_path=request.path,
                request_method=request.method,
                username=username,
            )
        except Exception:  # pylint: disable=broad-except
            logger.exception("Unexpected exception when recording user behavior")
        return None
