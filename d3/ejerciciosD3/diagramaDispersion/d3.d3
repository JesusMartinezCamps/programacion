var vis = {
  w : 500,
  h : 100,
  dataset : [
    [ 5,     20 ],
    [ 480,   90 ],
    [ 250,   50 ],
    [ 100,   33 ],
    [ 330,   95 ],
    [ 410,   12 ],
    [ 475,   44 ],
    [ 25,    67 ],
    [ 85,    21 ],
    [ 220,   88 ]
  ]
}

//Lista de datos

//Creacion del SVG
var svg = d3.select("body")
        .append("svg")
        .attr("width", vis.w)
        .attr("height", vis.h);

//Creacion de circulos
svg.selectAll("circle")
    .data(vis.dataset)
    .enter()
    .append("circle")
    .attr("cx", function(d) {
        return d[0];
    })
    .attr("cy", function(d) {
        return d[1];
    })
		.attr("r", function(d) {
			  return Math.sqrt(vis.h - d[1]);
		})
    
// Creacion de texto
svg.selectAll("text")
    .data(vis.dataset)
    .enter()
    .append("text")
    .text(function(d){
        return d[0] + "|" + d[1];
    })
     .attr("x", function(d){
        return d[0];
    })
    .attr("y", function(d){
        return d[1];
     })
     .attr("font-family", "sans-serif")
     .attr("font-size", "11px")
     .attr("fill", "darkred");