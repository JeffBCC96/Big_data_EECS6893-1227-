function randomHex(){
 var arrHex=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"],
     strHex="#";
     for(var i=0;i < 6; i++){
      strHex+=arrHex[Math.round(Math.random()*15)];
     }
 return strHex;
}



function line_1(chart_id, data_info){

    for (var i = 0; i< data_info['datasets'].length; i++){
        data_info['datasets'][i]['borderColor'] = randomHex()
    }

    var title_text = 'Keywords in cancer literature from 2009 to 2018 (index)'
    if (chart_id == 'line-chart_2'){
        title_text = 'Journals of cancer literature from 2009 to 2018 (index)'
    }

    new Chart(document.getElementById(chart_id), {
        type: 'line',
        data: data_info,
        options: {
            title: {
                display: true,
                text: title_text
            }
         }
    });


}

function pie_chart(pie_id, info, year){
    var bgcolor = []

    for (var i = 0; i< info['labels'].length; i++){
        new_color = randomHex()
        bgcolor.push(new_color)
    }

    info['datasets'][0]['backgroundColor'] = bgcolor

    new Chart(document.getElementById(pie_id), {
        type: 'pie',
        data: info,
        options: {
          title: {
            display: true,
            text: 'Keywords in ' + year
          },
          legend:{
            display: false
          },
        }
    });

}



function word_cloud(info){
  var data = info;

  // create a tag (word) cloud chart
  var chart = anychart.tagCloud(data);

   // set a chart title
  chart.title('10 topics in cancer literature')
  // set an array of angles at which the words will be laid out
  chart.angles([0])
  // enable a color range
  chart.colorRange(true);
  // set the color range length
  chart.colorRange().length('80%');
  chart.angles([0, -45, 90])
  chart.legend(true);
  chart.colorRange({orientation: "right"});

  // display the word cloud chart
  chart.container("lda_model");
  chart.draw();
};

