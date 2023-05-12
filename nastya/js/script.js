// Инициализация
new Swiper('.swiper-conteiner',{
    //стрелки
    navigation:{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
    },

    pagination:{
        el:'.swiper--pagination',
        clickable: true,
    },

    loop: true,
});
