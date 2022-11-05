import json
from random import randrange

from django.http import HttpResponse
from rest_framework.views import APIView

from pyecharts.charts import Bar, Pie, Map
from pyecharts.faker import Faker
from pyecharts import options as opts


# Create your views here.
def response_as_json(data):
    json_str = json.dumps(data)
    response = HttpResponse(
        json_str,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response


def json_response(data, code=200):
    data = {
        "code": code,
        "msg": "success",
        "data": data,
    }
    return response_as_json(data)


def json_error(error_string="error", code=500, **kwargs):
    data = {
        "code": code,
        "msg": error_string,
        "data": {}
    }
    data.update(kwargs)
    return response_as_json(data)


JsonResponse = json_response
JsonError = json_error


def pie_base() -> Pie:
    c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_colors(["blue", "green", "yellow", "red", "pink", "orange", "purple"])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
        .dump_options_with_quotes()
    )
    return c



def create_map():
    data = [['河北', 196], ['河南', 105], ['北京', 95]]
    m = (
        Map().add(
            series_name="人数",
            data_pair=data,
            maptype="china",
            is_map_symbol_show=False,
        )
        # 全局配置项
        .set_global_opts(
            # 设置标题
            title_opts=opts.TitleOpts(title="网站会员分布示意图"),
            # 设置标准显示
            visualmap_opts=opts.VisualMapOpts(max_=1000, is_piecewise=False),
            # 隐藏图例
            legend_opts=opts.LegendOpts(is_show=False),
        )
        # 系列配置项
        .set_series_opts(
            # 标签名称显示，默认为True
            label_opts=opts.LabelOpts(is_show=False, color="blue")
        )
        # .dump_options_with_quotes()
    )
    return m


class ChartView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(pie_base()))

class MapView(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(json.loads(create_map()))

class IndexView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(content=open("./templates/index.html").read())