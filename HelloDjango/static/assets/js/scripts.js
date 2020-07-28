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

for (let anchor of anchors) {
  anchor.addEventListener('click', function (e) {
    e.preventDefault()

    const blockID = anchor.getAttribute('href').substr(1)

    document.getElementById(blockID).scrollIntoView({
      behavior: 'smooth',
      block: 'start'
    })
  })
}

/*
Popap
 */

