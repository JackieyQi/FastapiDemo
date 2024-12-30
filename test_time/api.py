#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import time
from .router import router
from .schema import BannersResponse, BannersDate, Item


@router.get("/get_time", response_model=BannersResponse, summary="查询时间")
def get_time(name: str):
    # return f"{name}: {time.ctime()}"
    return BannersResponse(data=[
        BannersDate(img_url=str(time.ctime()), html_url=str(time.time())),
        ])


@router.post("/get_time", summary="查询时间")
def get_time(item: Item):
    result = []
    for i in item.data:
        result.append(time.ctime(i))
    return result

