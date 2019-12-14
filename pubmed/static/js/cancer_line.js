
function randomHex(){
 var arrHex=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"],
     strHex="#";
     for(var i=0;i < 6; i++){
      strHex+=arrHex[Math.round(Math.random()*15)];
     }
 return strHex;
}



function line_1(chart_id, data_info){

    for (var i = 0; i< data['datasets'].length; i++){
        data['datasets'][i]['borderColor'] = randomHex()
    }
    console.log(data_info)


    new Chart(document.getElementById(chart_id), {
        type: 'line',
        data: data_info
        options: {
            title: {
                display: true,
                text: 'Keywords for literature from 2008 to 2018 (counts)'
            }
         }
    });


}

function pie_chart(pie_id){

    new Chart(document.getElementById(pie_id), {
    type: 'pie',
    data: {
      labels: ["Africa", "Asia", "Europe", "Latin America", "North America"],
      datasets: [{
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
        data: [2478,5267,734,784,433]
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Predicted world population (millions) in 2050'
      }
    }
    });

}



function word_cloud(){
  var data = [
    {"x": "Mandarin chinese", "value": 1090000000, category: "Sino-Tibetan"},
    {"x": "English", "value": 983000000, category: "Indo-European"},
    {"x": "Hindustani", "value": 544000000, category: "Indo-European"},
    {"x": "Spanish", "value": 527000000, category: "Indo-European"},
    {"x": "Arabic", "value": 422000000, category: "Afro-Asiatic"},
    {"x": "Malay", "value": 281000000, category: "Austronesian"},
    {"x": "Russian", "value": 267000000, category: "Indo-European"},
    {"x": "Bengali", "value": 261000000, category: "Indo-European"},
    {"x": "Portuguese", "value": 229000000, category: "Indo-European"},
    {"x": "French", "value": 229000000, category: "Indo-European"},
    {"x": "Hausa", "value": 150000000, category: "Afro-Asiatic"},
    {"x": "Punjabi", "value": 148000000, category: "Indo-European"},
    {"x": "Japanese", "value": 129000000, category: "Japonic"},
    {"x": "German", "value": 129000000, category: "Indo-European"},
    {"x": "Persian", "value": 121000000, category: "Indo-European"}
  ];

 // create a tag (word) cloud chart
  var chart = anychart.tagCloud(data);

   // set a chart title
  chart.title('15 most spoken languages')
  // set an array of angles at which the words will be laid out
  chart.angles([0])
  // enable a color range
  chart.colorRange(true);
  // set the color range length
  chart.colorRange().length('80%');
  chart.angles([0, -45, 90])

  // display the word cloud chart
  chart.container("container");
  chart.draw();
};









//new Chart(document.getElementById("line-chart"), {
//  type: 'line',
//  data: {
//    labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
//    datasets: [{
//        data: [86,114,106,106,107,111,133,221,783,2478],
//        label: "Africa",
//        borderColor: "#3e95cd",
//        fill: false
//      }, {
//        data: [282,350,411,502,635,809,947,1402,3700,5267],
//        label: "Asia",
//        borderColor: "#8e5ea2",
//        fill: false
//      }, {
//        data: [168,170,178,190,203,276,408,547,675,734],
//        label: "Europe",
//        borderColor: "#3cba9f",
//        fill: false
//      }, {
//        data: [40,20,10,16,24,38,74,167,508,784],
//        label: "Latin America",
//        borderColor: "#e8c3b9",
//        fill: false
//      }, {
//        data: [6,3,2,2,7,26,82,172,312,433],
//        label: "North America",
//        borderColor: "#c45850",
//        fill: false
//      }
//    ]
//  },
//  options: {
//    title: {
//      display: true,
//      text: 'World population per region (in millions)'
//    }
//  }
//});