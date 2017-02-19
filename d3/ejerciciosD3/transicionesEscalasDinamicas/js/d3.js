// Variable vis con las variables globales
var vis = {}
    vis.w = 600;
    vis.h = 250;
    //Lista de Datos
    vis.dataset = [
      {key: 0, value: 5 },
      {key: 1, value: 10},
      {key: 2, value: 13},
      {key: 3, value: 19},
      {key: 4, value: 21},
      {key: 5, value: 25}, 
      {key: 6, value: 22}, 
      {key: 7, value: 18}, 
      {key: 8, value: 15}, 
      {key: 9, value: 13},
      {key: 10, value: 11}, 
      {key: 11, value: 12}, 
      {key: 12, value: 15}, 
      {key: 13, value: 20}, 
      {key: 14, value: 18}, 
      {key: 15, value: 17},
      {key: 16, value: 16}, 
      {key: 17, value: 18}, 
      {key: 18, value: 23}, 
      {key: 19, value: 25} ]; 

//Creacion de la escala X
var xScale = d3.scale.ordinal()
      .domain(d3.range(vis.dataset.length))
      .rangeRoundBands([0, vis.w], 0.05);
//Creacion de la escala Y
var yScale = d3.scale.linear()
      .domain([0, d3.max(vis.dataset, function(d){
           return d.value;
      })])
      .range([0, vis.h]);

//La key
var key = function(d){
  return d.key;
};

//Elemento SVG
var svg = d3.select("body")
     .append("svg")
     .attr("width", vis.w)
     .attr("height", vis.h);

//Creacion de las barras para la grafica
svg.selectAll("rect")
    .data(vis.dataset, key)
    .enter()
    .append("rect")
    .attr("x", function(d, i){
        return xScale(i);
    })
    .attr("y", function(d) {
        return vis.h - yScale(d.value);
    })
    .attr("width", xScale.rangeBand())
    .attr("height", function(d) {
         return yScale(d.value);
     })
     .attr("fill", function(d){
         return "rgb(100, 0, " + (d.value * 7) + ")";
     })
      .on("mouseover", function() {
         d3.select(this)
           .attr("fill", function(d){
               return "rgb(150, 40, " + (d.value * 15) + ")";
           })
       })
      .on("mouseout", function(d) {
          d3.select(this)
              .transition()
              .duration(250)
              .attr("fill", function(d){
                 return "rgb(100, 0, " + (d.value * 7) + ")";
              })
       });

//Creacion de texto
svg.selectAll("text")
    .data(vis.dataset, key)
    .enter()
    .append("text")
    .text(function(d){
        return d.value;
    })
    .attr("x", function(d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
    })
    .attr("y", function(d){
        return vis.h - yScale(d.value) + 14;
    })
    .attr("text-anchor", "middle")
    .attr("fill", "white")

//CODIGO PARA AÑADIR Y QUITAR BARRAS//
	d3.selectAll("p")
			    .on("click", function() {
			        var paragraphID = d3.select(this).attr("id");
			        if (paragraphID == "add") {
			           
			            var maxValue = 25;
			            var newNumber = Math.floor(Math.random() * maxValue);
			            var lastKeyValue = vis.dataset[vis.dataset.length - 1].key;
			            console.log(lastKeyValue);
			            vis.dataset.push({
			                key: lastKeyValue + 1,
			                value: newNumber
			            });
			        } else {
			            vis.dataset.shift();
			        }

			        //Actualizacion de las escalas para los nuevos valores
			        xScale.domain(d3.range(vis.dataset.length));
			        yScale.domain([0, d3.max(vis.dataset, function(d) {
			            return d.value;
			        })]);

			        //Select de la nueva barra
			        var bars = svg.selectAll("rect")
			            .data(vis.dataset, key);

			        //Entrada de la nueva barra
			        bars.enter()
			            .append("rect")
			            .attr("x", vis.w)
			            .attr("y", function(d) {
			                return vis.h - yScale(d.value);
			            })
			            .attr("width", xScale.rangeBand())
			            .attr("height", function(d) {
			                return yScale(d.value);
			            })
			            .attr("fill", function(d) {
			                return "rgb(100, 0, " + (d.value * 7) + ")";
			            })
                  .on("mouseover", function() {
                     d3.select(this)
                       .attr("fill", function(d){
                           return "rgb(150, 40, " + (d.value * 15) + ")";
                       })
                   })
                  .on("mouseout", function(d) {
                      d3.select(this)
                          .transition()
                          .duration(250)
                          .attr("fill", function(d){
                             return "rgb(100, 0, " + (d.value * 7) + ")";
                          })
                   });

			        //Actualizacion de la nueva barra
			        bars.transition()
			            .duration(500)
			            .attr("x", function(d, i) {
			                return xScale(i);
			            })
			            .attr("y", function(d) {
			                return vis.h - yScale(d.value);
			            })
			            .attr("width", xScale.rangeBand())
			            .attr("height", function(d) {
			                return yScale(d.value);
			            });
    

			        //Borrar la barra de la izquierda
			        bars.exit()
			            .transition()
			            .duration(500)
			            .attr("x", -xScale.rangeBand())
			            .remove();
    
			        //Seleccionar el texto creado
			        var labels = svg.selectAll("text")
			            .data(vis.dataset, key);

			        //Enter para el nuevo texto
			        labels.enter()
			            .append("text")
			            .text(function(d) {
			                return d.value;
			            })
			            .attr("text-anchor", "middle")
			            .attr("x", vis.w)
			            .attr("y", function(d) {
			                return vis.h - yScale(d.value) + 14;
			            })
			            .attr("fill","white")

			        //actualizacion para el nuevo texto
			        labels.transition()
			            .duration(500)
			            .attr("x", function(d, i) {
			                return xScale(i) + xScale.rangeBand() / 2;
			            });

			        //Salida del texto de la izquierda
			        labels.exit()
			            .transition()
			            .duration(500)
			            .attr("x", -xScale.rangeBand())
			            .remove();
			    });