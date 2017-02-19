      //Variable vis
      var vis = {
          w : 500,
          h : 300,
          padding : 30,
          dataset : [
                  [5, 20], [480, 90], [250, 50], [100, 33], [330, 95],
                  [410, 12], [475, 44], [25, 67], [85, 21], [600, 150], [220, 88]
                  ]
      }

			//Creacion de las escalas
			var xScale = d3.scale.linear()
								 .domain([0, d3.max(vis.dataset, function(d) { return d[0]; })])
								 .range([vis.padding, vis.w - vis.padding * 2]);

			var yScale = d3.scale.linear()
								 .domain([0, d3.max(vis.dataset, function(d) { return d[1]; })])
								 .range([vis.h - vis.padding, vis.padding]);
      
      var rScale = d3.scale.linear()
                 .domain([0, d3.max(vis.dataset, function(d) {return d[1]; })])
                 .range([2, 5]);

	    //Creacion de los ejes
      var xAxis = d3.svg.axis()
                .scale(xScale)
                .orient("bottom")
                .ticks(5);      //Numero de marcadores aproximado
      var yAxis = d3.svg.axis()
                .scale(yScale)
                .orient("left")
                .ticks(5);      //Numero de marcadores aproximado

			//Creacion del SVG
			var svg = d3.select("body")
						.append("svg")
						.attr("width", vis.w)
						.attr("height", vis.h);

      //Creacion de los circulos
			svg.selectAll("circle")
			   .data(vis.dataset)
			   .enter()
			   .append("circle")
			   .attr("cx", function(d) {
			   		return xScale(d[0]);
			   })
			   .attr("cy", function(d) {
			   		return yScale(d[1]);
			   })
			   .attr("r", function(d) {
			   		return rScale(d[1]*2);
			   });
      
      
      //Creacion del texto
/*
			svg.selectAll("text")
			   .data(vis.dataset)
			   .enter()
			   .append("text")
			   .text(function(d) {
			   		return d[0] + " | " + d[1];
			   })
			   .attr("x", function(d) {
			   		return xScale(d[0]);
			   })
			   .attr("y", function(d) {
			   		return yScale(d[1]);
			   })
			   .attr("font-family", "sans-serif")
			   .attr("font-size", "11px")
			   .attr("fill", "blue");
         */

        //Creacion de x e y Axis
        svg.append("g")
            .attr("class", "axis")    //Asigna la clase "axis"
            .attr("transform", "translate(0," + (vis.h - vis.padding) + ")")      //Colocar el eje en la parte de abajo
            .call(xAxis);

        svg.append("g")
            .attr("class", "axis")    //Asigna la clase "axis"
            .attr("transform", "translate(" + vis.padding + ",0)")      //Colocar el eje en la parte izquierda
            .call(yAxis);