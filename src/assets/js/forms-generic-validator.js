'use strict';

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    let fv; // Declare fv in a scope accessible to both initialization and event listeners
    var inputs = document.querySelectorAll('input');

    //Exibe calendário em campos de data
    for (var iCont = 0; iCont < inputs.length; iCont++) {



      var TransactionDate = $('#' + inputs[iCont].name);

      // Transaction Date (flatpicker)
      if (TransactionDate) {
        TransactionDate.flatpickr({
          monthSelectorType: 'static',
          dateFormat: 'd/m/Y',
          onClose: function () {
            fv.revalidateField(inputs[iCont].id);
          }
        });
      }

    }


    var select2 = $('.select2');

    if (select2.length) {
      select2.each(function () {
        var $this = $(this);
        select2Focus($this);
        $this.wrap('<div class="position-relative"></div>').select2({
          placeholder: 'Selecione uma opção na lista',
          dropdownParent: $this.parent()
        });

        // Add event listener to clear validation messages on input change
        $this.on('change', function () {
          fv.revalidateField('status');
        });
      });
    }


  })();
});
