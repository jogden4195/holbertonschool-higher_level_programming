$(function () {
  let lang = $('html').attr('lang');
  $.get('https://fourtonfish.com/hellosalut/?lang=' + lang, function (data) {
    $('DIV#hello').append('<p>' + data.hello + '</p>');
  });
});
