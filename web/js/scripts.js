(function(window, document, undefined){

  window.onload = init;

  function init(){
    var g = document.getElementById('graph');

    Plotly.d3.json('FreqData/BeardedGQ.json', function(error, rawdata) {
      if (error) g.innerHTML = error;

      var trace1 = {
        x:rawdata[0],
        y:rawdata[1],
        marker: {color: "rgba(142,189,42,0.9)"},
        name: "B18_LR_hdh",
        type: "bar"
      }

      g.innerHTML = "Works"
    })
  }



})(window, document, undefined); 