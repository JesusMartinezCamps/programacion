/*variables*/
var w = 700;
var h = 150;
var barPadding = 25;
var dataset = [8, 14, 15, 15, 23];

var svg = d3.select("svg")
.append("svg")
.attr("width", w)
.attr("height", h);
/*Rango con los años*/
var xScale = d3.scale.linear()
.domain([2012.6, 2017.4])
.range([0, w - barPadding]);
/*Lista de los años*/
var xAxis = d3.svg.axis()
.scale(xScale)
.tickValues([2013, 2014, 2015, 2016, 2017])
.ticks(5);

svg.selectAll("rect")
  .data(dataset)
  .enter()
  .append("rect")
  .attr("x", function(d, i) {
  return i * (w / dataset.length);
})
  .attr("y", function(d) {
  return h - (d * 6 + barPadding);
})
  .attr("width", w / dataset.length - barPadding)
  .attr("height", function(d) {
  return d * 4;
})
  .attr("fill", function(d) {
  return "red";
});
/*detalles del texto rojo*/
svg.selectAll("text")
  .data(dataset)
  .enter()
  .append("text")
  .text(function(d) {
  return d;
})
  .attr("x", function(d, i) {
  return i * (w / dataset.length) + (w / dataset.length - barPadding)/1.5;
})
  .attr("y", function(d) {
  return h - (d * 4) - 30;
})
  .attr("font-family", "sans-serif")
  .attr("font-size", "11px")
  .attr("text-anchor", "middle")
  .attr("fill", "white")

/*Lista con el numero de alumnos*/
var dataset = [7, 10, 10, 12, 15];
var svg = d3.select("svg")
.append("svg")
.attr("width", w)
.attr("height", h);

svg.selectAll("rect")
  .data(dataset)
  .enter()
  .append("rect")
  .attr("x", function(d, i) {
  return i * (w / dataset.length);
})
  .attr("y", function(d) {
  return h - (d * 4 + barPadding);
})
  .attr("width", w / dataset.length - barPadding)
  .attr("height", function(d) {
  return d *4;
})
  .attr("fill", function(d) {
  return "blue"
});
/*detalles del texto azul*/
svg.selectAll("text")
  .data(dataset)
  .enter()
  .append("text")
  .text(function(d) {
  return d;
})
  .attr("x", function(d, i) {
  return i * (w / dataset.length) + (w / dataset.length - barPadding) / 4;
})
  .attr("y", function(d) {
  return h - (d * 4) - 5;
})
  .attr("font-family", "sans-serif")
  .attr("font-size", "11px")
  .attr("text-anchor", "middle")
  .attr("fill", "white");

svg.append("g")
  .attr("class","axis")
  .attr("transform", "translate(0," + (h - barPadding  ) + ")")
  .call(xAxis);