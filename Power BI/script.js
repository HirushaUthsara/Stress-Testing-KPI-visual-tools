var iframe = document.getElementById('report');
var start = performance.now();

iframe.onload = function() {
  var end = performance.now();
  var loadTime = end - start;
  console.log('Load time: ' + loadTime + 'ms');
};
