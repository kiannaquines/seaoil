'use strict';

(function () {
  let cardColor, headingColor, axisColor, shadeColor, borderColor;

  cardColor = config.colors.cardColor;
  headingColor = config.colors.headingColor;
  axisColor = config.colors.axisColor;
  borderColor = config.colors.borderColor;

  const totalRevenueChartElement = document.querySelector('#totalRevenueChart');

  fetch("fetchTotalSalesMonthly/")
  .then(response => response.json())
  .then(jsonData => {
    const years = Object.keys(jsonData);
    const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    const series = years.map(year => ({
      name: year,
      data: months.map(month => {
        const entry = jsonData[year].find(item => item.month === month);
        return entry ? entry.total : 0;
      })
    }));

    const options = {
      series: series,
      chart: {
        height: 350,
          type: 'area',
          fontFamily: 'Public Sans, Arial, sans-serif',
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'smooth'
      },
      colors: [config.colors.warning,config.colors.primary],
      xaxis: {
        categories: months,
        labels: {
          style: {
            fontSize: '13px',
            colors: '#95A2AF'
          }
        },
      },
      yaxis: {
        labels: {
          style: {
            fontSize: '13px',
            colors: '#95A2AF'
          }
        }
      },
    };

    var totalRevenueChart = new ApexCharts(totalRevenueChartElement, options);
    totalRevenueChart.render();
  }).catch(error => console.error('Error fetching data:', error));

  const productInChartElement = document.querySelector('#productMonthlyIn');
  fetch('fetchTotalProductIn/')
    .then(response => response.json())
    .then(data => {
      const categories = data.map(item => item.month);
      const seriesData = data.map(item => item.total);
  
      var options = {
        series: [{
          name: 'Monthly Warehouse Product In',
          data: seriesData,
        }],
        chart: {
          height: 350,
          type: 'area',
          fontFamily: 'Public Sans, Arial, sans-serif',
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        colors: [config.colors.primary],
        xaxis: {
          categories: categories,
          labels: {
            style: {
              fontSize: '13px',
              colors: '#95A2AF'
            }
          },
        },
        yaxis: {
          labels: {
            style: {
              fontSize: '13px',
              colors: '#95A2AF'
            }
          }
        },
      };  
      const productInChart = new ApexCharts(productInChartElement, options);
      productInChart.render();
    }).catch(error => console.error('Error fetching data:', error));
})();
