$( document ).ready(function() {
    new WOW().init();
  });

/*
Инициализаяция таблиц
 */
$(document).ready(function () {
$('#dtBasicExample').DataTable();
$('.dataTables_length').addClass('bs-select');
});

/*
Отрисовка оценки жюри
 */
function GetRating(x) {
    $('#jury-rating').text(`${x} / 10`);
}

/*
Partners Slider
 */
$(document).ready(function() {
    $('.partners-slider').slick({
        dots: true,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        slidesToScroll: 1,
        arrows: false,
        responsive: [
            {
                breakpoint: 1024,
                settings: {
                    slidesToShow: 3,
                    slidesToScroll: 1,
                    infinite: true,
                    dots: true
                }
            },
            {
                breakpoint: 600,
                settings: {
                    slidesToShow: 2,
                    slidesToScroll: 1
                }
            },
            {
                breakpoint: 480,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ]
    });
});

/*
Сортировка заявок по категориям
 */
let select_on = document.getElementById('nomination-select');

select_on.addEventListener('change', async function(){
      let getValue = this.value;
      // this в этом контексте - элемент, который запустил фукнцию. То же, что и select.value;
      console.log( getValue );
      $('.request-card').fadeOut();
      $('.request-card[data-nomination="' + getValue + '"]').fadeIn();
      if (getValue == 'Все номинации') {
          $('.request-card').fadeIn();
      }
    });


