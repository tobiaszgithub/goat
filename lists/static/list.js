var initialize = function () {
  $('input[name="text"]').on('keypress', function () {
    $('input[name="text"]').removeClass('is-invalid');
  });
};