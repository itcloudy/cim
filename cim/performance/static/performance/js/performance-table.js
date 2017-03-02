$.extend($.fn.bootstrapTable.defaults, {
    method: "post",
    dataType: "json",
    locale: "zh-CN",
    contentType: "application/x-www-form-urlencoded",
    sidePagination: "server",
    stickyHeader: true, //表头固定
    stickyHeaderOffsetY: (function() {
        'use strict';
        var stickyHeaderOffsetY = 0;
        if ($('.navbar-fixed-top').css('height')) {
            stickyHeaderOffsetY = +$('.navbar-fixed-top').css('height').replace('px', '');
        }
        if ($('.navbar-fixed-top').css('margin-bottom')) {
            stickyHeaderOffsetY += +$('.navbar-fixed-top').css('margin-bottom').replace('px', '');
        }
        return stickyHeaderOffsetY + 'px';
    })(), //设置偏移量
    dataField: "data",
    pagination: true,
    pageNumber: 1,
    pageSize: 20,
    pageList: [10, 25, 50, 100, 500, 1000],
    // onClickRow: function(row, $element) {
    //     //$element是当前tr的jquery对象
    //     $element.css("background-color", "green");
    // }, //单击row事件
    onCheck: function(row, $el) {
        $($el[0].parentNode.parentNode).addClass("danger");
    },
    onUncheck: function(row, $el) {
        $($el[0].parentNode.parentNode).removeClass("danger");
    },
    onCheckAll: function(rows) {
        $("#display-table tbody>tr").addClass("danger");
    },
    onUncheckAll: function(rows) {
        $("#display-table tbody>tr").removeClass("danger");
    }
});
function defaultQueryParams(params) {
    return params;
};
var displayTable = function(selectId, ajaxUrl, columns, bootstrapTableFunctionDict) {
    var $tableNode = $(selectId);
    var queryParams = defaultQueryParams;
    var onExpandRow = undefined;
    var onPostBody = undefined;
    if (bootstrapTableFunctionDict != undefined) {
        if (bootstrapTableFunctionDict.onExpandRow != undefined) {
            onExpandRow = bootstrapTableFunctionDict.onExpandRow;
        }
        if (bootstrapTableFunctionDict.onPostBody != undefined) {
            onPostBody = bootstrapTableFunctionDict.onPostBody;
        }
        if (bootstrapTableFunctionDict.queryParams) {
            queryParams = bootstrapTableFunctionDict.queryParams;
        }
    }


    var options = {
        url: ajaxUrl,
        queryParams: queryParams,
        columns: columns
    }
    if (onExpandRow != undefined) {
        options.detailView = true;
        options.onExpandRow = onExpandRow;
    }
    if (onPostBody != undefined) {
        options.onPostBody = onPostBody;
    }

    $tableNode.bootstrapTable(options);
    // 选中行颜色变化
    // $("#display-table .bs-checkbox").on('click', function(e) {
    //     console.log(e);
    // });
};
displayTable("#performance-table", '/performance/', [
    { title: "全选", field: 'ID', checkbox: true, align: "center", valign: "middle" },
    { title: "公司名称", field: 'Name', sortable: true, order: "desc" },
    { title: "公司编码", field: 'Code', sortable: true, order: "desc" },
    { title: "母公司", field: 'Parent', sortable: true, order: "desc" },
    { title: "公司地址", field: 'Address' },
    {
        title: "操作",
        align: "center",
        field: 'action',
        formatter: function cellStyle(value, row, index) {
            var html = "";
            var url = "/company/";
            html += "<a href='" + url + row.id + "?action=edit' class='table-action btn btn-xs btn-default'>编辑<i class='fa fa-pencil'></i></a>";
            html += "<a href='" + url + row.id + "?action=detail' class='table-action btn btn-xs btn-default'>详情<i class='fa fa-external-link'></i></a>";
            return html;
        }
    }
]);