import pyecharts.options as opts
from pyecharts.charts import Scatter

"""
def add_yaxis(
        # 系列名称，用于 tooltip 的显示，legend 的图例筛选。
        series_name: str,

        # 系列数据
        y_axis: Sequence,

        # 是否选中图例
        is_selected: bool = True,

        # 使用的 x 轴的 index，在单个图表实例中存在多个 x 轴的时候有用。
        xaxis_index: Optional[Numeric] = None,

        # 使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用。
        yaxis_index: Optional[Numeric] = None,

        # 系列 label 颜色
        color: Optional[str] = None,

        # 标记的图形。
        # ECharts 提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle', 
        # 'diamond', 'pin', 'arrow', 'none'
        # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
        symbol: Optional[str] = None,

        # 标记的大小，可以设置成诸如 10 这样单一的数字，也可以用数组分开表示宽和高，
        # 例如 [20, 10] 表示标记宽为 20，高为 10。
        symbol_size: Numeric = 10,

        # 标记的旋转角度。注意在 markLine 中当 symbol 为 'arrow' 时会忽略 symbolRotate 强制设置为切线的角度。
        symbol_rotate: types.Optional[types.Numeric] = None,

        # 标签配置项，参考 `series_options.LabelOpts`
        label_opts: Union[opts.LabelOpts, dict] = opts.LabelOpts(position="right"),

        # 标记点配置项，参考 `series_options.MarkPointOpts`
        markpoint_opts: Union[opts.MarkPointOpts, dict, None] = None,

        # 标记线配置项，参考 `series_options.MarkLineOpts`
        markline_opts: Union[opts.MarkLineOpts, dict, None] = None,

        # 图表标域，常用于标记图表中某个范围的数据，参考 `series_options.MarkAreaOpts`
        markarea_opts: types.MarkArea = None,

        # 提示框组件配置项，参考 `series_options.TooltipOpts`
        tooltip_opts: Union[opts.TooltipOpts, dict, None] = None,

        # 图元样式配置项，参考 `series_options.ItemStyleOpts`
        itemstyle_opts: Union[opts.ItemStyleOpts, dict, None] = None,

        # 可以定义 data 的哪个维度被编码成什么。
        encode: types.Union[types.JSFunc, dict, None] = None,
)

class ScatterItem(
    # 数据项名称。
    name: Union[str, Numeric] = None,
 
    # 数据项值。
    value: Union[str, Numeric] = None,
 
    # 单个数据标记的图形。
    # ECharts 提供的标记类型包括 
    # 'circle', 'rect', 'roundRect', 'triangle', 'diamond', 'pin', 'arrow', 'none'
    # 可以通过 'image://url' 设置为图片，其中 URL 为图片的链接，或者 dataURI。
    # 可以通过 'path://' 将图标设置为任意的矢量路径。
    symbol: Optional[str] = None,
 
    # 单个数据标记的大小，可以设置成诸如 10 这样单一的数字
    # 也可以用数组分开表示宽和高，例如 [20, 10] 表示标记宽为20，高为10。
    symbol_size: Union[Sequence[Numeric], Numeric] = None,
 
    # 单个数据标记的旋转角度（而非弧度）。正
    symbol_rotate: Optional[Numeric] = None,
 
    # 如果 symbol 是 path:// 的形式，是否在缩放时保持该图形的长宽比。
    symbol_keep_aspect: bool = False,
 
    # 单个数据标记相对于原本位置的偏移。
    symbol_offset: Optional[Sequence] = None,
 
    # 标签配置项，参考 `series_options.LabelOpts`
    label_opts: Union[LabelOpts, dict, None] = None,
 
    # 图元样式配置项，参考 `series_options.ItemStyleOpts`
    itemstyle_opts: Union[ItemStyleOpts, dict, None] = None,
 
    # 提示框组件配置项，参考 `series_options.TooltipOpts`
    tooltip_opts: Union[TooltipOpts, dict, None] = None,
)
"""

def create_scatter():
#     x = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月']
#     y = [8, 5, 3, 4, 8, 2, 2, 5, 1]
#     (
#         Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
#         .add_xaxis(x)
#         .add_yaxis("", y)
#         .set_global_opts(
#
#         )
#
#     )
    data = [
        [10.0, 8.04],
        [8.0, 6.95],
        [13.0, 7.58],
        [9.0, 8.81],
        [11.0, 8.33],
        [14.0, 9.96],
        [6.0, 7.24],
        [4.0, 4.26],
        [12.0, 10.84],
        [7.0, 4.82],
        [5.0, 5.68],
    ]
    data.sort(key=lambda x: x[0])
    x_data = [d[0] for d in data]
    y_data = [d[1] for d in data]
    y_data_1 = [1 for _ in data]
    (
        Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol_size=40,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .add_yaxis(
            series_name="",
            y_axis=y_data_1,
            symbol_size=10,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_series_opts()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="气泡图"),
            visualmap_opts=opts.VisualMapOpts(range_opacity=0.45,
                                              type_="size",
                                              max_=10,
                                              is_piecewise=True),
            xaxis_opts=opts.AxisOpts(
                type_="value", splitline_opts=opts.SplitLineOpts(is_show=True)
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            tooltip_opts=opts.TooltipOpts(is_show=True),
        )
        .render("留存率.html")
    )


create_scatter()