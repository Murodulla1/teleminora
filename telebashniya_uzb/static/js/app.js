new Splide('.popular', {
    type: 'loop',
    perPage: 1,
    arrows: false,
    autoplay: true,
    interval: 5000,
}).mount();

document.querySelector('.header__btn').addEventListener('click',function(event){
    document.querySelector('.header__menu').classList.toggle('active');
});