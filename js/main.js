// Tiny Terra Spaces Guide - Shared JavaScript

// Generate sitemap-like navigation highlighting
document.addEventListener('DOMContentLoaded', function() {
  var path = window.location.pathname;
  var navLinks = document.querySelectorAll('.main-nav a');
  navLinks.forEach(function(a) {
    if (a.getAttribute('href') !== '/' && path.indexOf(a.getAttribute('href')) === 0) {
      a.classList.add('curr');
    } else if (a.getAttribute('href') === '/' && (path === '/' || path === '/index.html')) {
      a.classList.add('curr');
    }
  });

  // Language highlighting
  var langLinks = document.querySelectorAll('.lang-nav a');
  langLinks.forEach(function(a) {
    var href = a.getAttribute('href');
    if (href === '/' + getLangPrefix() + '/') {
      a.classList.add('curr');
    }
  });
});

function getLangPrefix() {
  var path = window.location.pathname;
  var match = path.match(/^\/([a-z]{2})\//);
  return match ? match[1] : '';
}
