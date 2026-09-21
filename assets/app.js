(function(){
  "use strict";
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- header sticky con reducción de altura ---- */
  var hdr = document.getElementById('hdr'), ticking = false;
  function onScroll(){
    if(ticking) return; ticking = true;
    requestAnimationFrame(function(){
      hdr.classList.toggle('stuck', window.scrollY > 24);
      ticking = false;
    });
  }
  window.addEventListener('scroll', onScroll, {passive:true}); onScroll();

  /* ---- menú mobile ---- */
  var burger = document.getElementById('burger'),
      mnav = document.getElementById('mnav'),
      bIcon = document.getElementById('burger-i');
  function setMenu(open){
    mnav.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    burger.setAttribute('aria-label', open ? 'Cerrar menú' : 'Abrir menú');
    bIcon.innerHTML = '<use href="#' + (open ? 'i-close' : 'i-menu') + '"/>';
  }
  burger.addEventListener('click', function(){ setMenu(!mnav.classList.contains('open')); });
  mnav.addEventListener('click', function(e){ if(e.target.closest('a')) setMenu(false); });
  document.addEventListener('keydown', function(e){ if(e.key === 'Escape') setMenu(false); });

  /* ---- scroll reveal ---- */
  var items = document.querySelectorAll('[data-reveal]');
  if(reduce || !('IntersectionObserver' in window)){
    items.forEach(function(el){ el.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, {rootMargin:'0px 0px -8% 0px', threshold:.12});
    items.forEach(function(el){ io.observe(el); });
  }

  /* ---- parallax 3D suave con el mouse ---- */
  if(!reduce && window.matchMedia('(pointer:fine)').matches){
    document.querySelectorAll('.scene').forEach(function(scene){
      var inner = scene.querySelector('.scene-in');
      if(!inner) return;
      scene.addEventListener('mousemove', function(e){
        var r = scene.getBoundingClientRect(),
            x = (e.clientX - r.left) / r.width - .5,
            y = (e.clientY - r.top) / r.height - .5;
        inner.style.transition = 'transform .18s linear';
        inner.style.transform = 'rotateY(' + (x * 11).toFixed(2) + 'deg) rotateX(' + (-y * 9).toFixed(2) + 'deg)';
      });
      scene.addEventListener('mouseleave', function(){
        inner.style.transition = 'transform .9s cubic-bezier(.22,1,.36,1)';
        inner.style.transform = '';
      });
    });
  }

  /* ---- mapa diferido (no penaliza el LCP) ---- */
  var mapCard = document.getElementById('mapCard');
  function loadMap(){
    if(!mapCard || mapCard.dataset.loaded) return;
    mapCard.dataset.loaded = '1';
    var f = document.createElement('iframe');
    f.src = 'https://maps.google.com/maps?q=' +
            encodeURIComponent('-25.3465404,-57.6000046 (Policlínica Sanitas)') +
            '&z=17&output=embed';
    f.title = 'Mapa con la ubicación de la Policlínica Sanitas en Lambaré';
    f.loading = 'lazy';
    f.referrerPolicy = 'no-referrer-when-downgrade';
    f.allowFullscreen = true;
    mapCard.appendChild(f);
  }
  if(mapCard){
    if('IntersectionObserver' in window){
      var mio = new IntersectionObserver(function(en){
        if(en[0].isIntersecting){ loadMap(); mio.disconnect(); }
      }, {rootMargin:'320px'});
      mio.observe(mapCard);
    } else { loadMap(); }
  }

  /* ---- eventos para los píxeles de anuncios ----------------------------
     Se disparan sólo si el píxel está cargado. No se envía el motivo de
     consulta ni la especialidad: son datos de salud y las plataformas de
     anuncios prohíben recibirlos. Sólo viaja la sección de la página.      */
  function evento(nombreMeta, nombreGoogle, datos){
    try{
      if(typeof window.fbq === 'function') window.fbq('track', nombreMeta, datos || {});
      if(typeof window.gtag === 'function') window.gtag('event', nombreGoogle, datos || {});
      if(Array.isArray(window.dataLayer)) window.dataLayer.push(
        Object.assign({event: nombreGoogle}, datos || {}));
    }catch(err){ /* nunca romper la página por un píxel */ }
  }

  document.addEventListener('click', function(ev){
    var a = ev.target && ev.target.closest ? ev.target.closest('a[href]') : null;
    if(!a) return;
    var href = a.getAttribute('href') || '';
    var seccion = 'general';
    if(a.closest){
      var sec = a.closest('section');
      if(a.classList.contains('wa-float')) seccion = 'boton-flotante';
      else if(a.closest('.wa-bar'))        seccion = 'barra-mobile';
      else if(a.closest('.hdr'))           seccion = 'header';
      else if(a.closest('.mnav'))          seccion = 'menu-mobile';
      else if(a.closest('.ftr'))           seccion = 'footer';
      else if(sec && sec.id)               seccion = sec.id;
    }
    if(href.indexOf('https://wa.me/') === 0){
      evento('Contact', 'contacto_whatsapp', {seccion: seccion});
    } else if(href.indexOf('google.com/maps') > -1){
      evento('FindLocation', 'como_llegar', {seccion: seccion});
    }
  }, true);

  /* las páginas por especialidad avisan que se vieron */
  if(window.SANITAS_PAGINA){
    evento('ViewContent', 'ver_especialidad', {seccion: window.SANITAS_PAGINA});
  }

  /* ---- link activo en el menú ---- */
  var secs = ['inicio','profesionales','especialidades','estudios','turnos','ubicacion']
    .map(function(id){ return document.getElementById(id); }).filter(Boolean);
  if('IntersectionObserver' in window && secs.length){
    var links = document.querySelectorAll('.nav a');
    var sio = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(!en.isIntersecting) return;
        links.forEach(function(a){
          var on = a.getAttribute('href') === '#' + en.target.id;
          a.style.color = on ? 'var(--red-800)' : '';
          a.style.background = on ? 'var(--rose-50)' : '';
        });
      });
    }, {rootMargin:'-45% 0px -50% 0px'});
    secs.forEach(function(s){ sio.observe(s); });
  }
})();
