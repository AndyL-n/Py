from pyecharts import options as opts
from pyecharts.charts import Map


data = [['河北', 196], ['河南', 105], ['北京', 95]]

def create_map():
    (
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
        # 生成本地html文件
        .render("网站会员分布示意图.html")
    )


create_map()