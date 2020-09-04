$(document).ready(function () {
  $.browser = $.browser || {};
  $('.date').datepick({ dateFormat: 'yy-mm-dd' });
});

/**
 * 跳转到路由页面
 * @param {*} routeName 
 */
function route(routeName) {
  location.href = routeName;
}
