Chart.register(ChartDataLabels);

// const data = {
//   labels: ["Hommes", "Femmes","trans"],
//   datasets: [{
//     data: [20, 45, 35 ],
//     backgroundColor: ["#3498db", "#e91e63","#10c66eda"],
//     hoverOffset: 15
//   }]
// };
const pieData = JSON.parse(
  document.getElementById('pie_data').textContent
);
console.log(pieData);
const config = {
  type: "doughnut",
  data: {
    labels: pieData.labels,
    datasets:[{
      data: pieData.values,
      backgroundColor:['#213A57','#0B6477','#14919B','#0AD1C8','#45DFB1'],
      hoverOffset: 15
    }]
  },
  options: {
    cutout: "55%",
    responsive: true,
    maintainAspectRatio:false,
    plugins: {

      /* 🔹 Pourcentages sur le donut */
      datalabels: {
        color: "#fff",
        font: {
          weight: "bold",
          size: 9
        },
        formatter: (value, ctx) => {
          const total = ctx.chart.data.datasets[0].data
            .reduce((a, b) => a + b, 0);
          return Math.round(value * 100 / total) + "%";
        }
      },

      /* 🔹 Tooltip */
      tooltip: {
        callbacks: {
          label: function(context) {
            return context.label +' : '+
                    pieData.pourcentage[context.dataIndex]+ '%'
          }
        }
      },

      /* 🔹 Légende à droite + ronds */
      legend: {
        position: "right",
        display:true,
        labels: {
          usePointStyle: true,      // nécessaire pour dessiner le cercle
          pointStyle: "circle",     // type de symbole
          color: "black",
          padding: 8,
          font: { size: 13 },       // taille du texte
          pointStyleWidth: 20
        }
      },
    }
  }
};

const centerTextPlugin = {
    id: 'centerText',
    beforeDraw(chart) {
      const { ctx, chartArea } = chart;
      const centerX = (chartArea.left + chartArea.right) / 2;
      const centerY = (chartArea.top + chartArea.bottom) / 2;
  
      ctx.save();
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
  
      ctx.font = 'bold 14px Arial';
      ctx.fillStyle = '#073B4C';
      ctx.fillText('Moy', centerX, centerY - 10);
  
      ctx.font = '14px Arial';
      ctx.fillStyle = '#118AB2';
      ctx.fillText(pieData.moyenne+'ans', centerX, centerY + 12);
  
      ctx.restore();
    }
  };

// new Chart(document.getElementById("donutChart"), config);

new Chart(document.getElementById("donutChart"), {
    ...config,
    plugins: [centerTextPlugin] // 👈 ici
  });

const barData = JSON.parse(
  document.getElementById("bar_data").textContent
);
const donnee = {
  labels: ["haut gradé","sous-offi" ,"gradé"],
  datasets: [
    {
      label: "Homme",
      data: barData.homme,
      backgroundColor: "#2109a8",
      borderRadius: 6,
    //   barThickness: 20 
    },
    {
      label: "Femme",
      data: barData.femme,
      backgroundColor: "#5c0aa8",
      borderRadius: 6,
    //   barThickness: 20
    }
  ]
};

const confi = {
    type: "bar",
    data: donnee,
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        title: {
            display: false,              // Affiche le titre
            text: 'Repartition de grade', // Texte du titre
            color: '#0a011f',             // Couleur du texte
            font: {
              size: 15,
              weight: 'bold'
            },
            padding: {
              top: 2,
              bottom: 20
            }
        },
        legend: {
          display: true,
          position: "top",
          labels: {
            color: "#0a011f",
            usePointStyle: true,
            pointStyle: "circle",
            padding: 15,
            font:{size: 13 , weight:"bold"}
          }
        },
        // 🔹 Labels sur les barres
      datalabels: {
        color: "#4d0ec1",
        anchor: "end",
        align: "end",
        font: {
          weight: "bold",
          size: 10
        },
        formatter: (value) => value
      },
       tooltip: {
          mode: "index",
          intersect: false
        }
      },
  
      scales: {
        x: {
            // barPercentage: 0.05,
            // categoryPercentage: 0.8,
            grid: { display: false },
            ticks: { 
                color: "#07011a",
                font:{
                    weight:'bold',
                    family:'Arial'
                }
            }
          },
          y: {
            grid: { display: false },
            ticks: { display: false},
            beginAtZero: true
          }
      },
      animation: {
        duration: 1500,
        easing: "easeInOutQuart"
      }
    }
  };

console.log(barData)
  
new Chart(document.getElementById("areaChart"), confi);
  