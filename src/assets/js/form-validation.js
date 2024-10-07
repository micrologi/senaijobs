'use strict';

(function () {
  // Init custom option check
  window.Helpers.initCustomOptionCheck();

  // Bootstrap validation example
  //------------------------------------------------------------------------------------------
  // const flatPickrEL = $('.flatpickr-validation');
  const flatPickrList = [].slice.call(document.querySelectorAll('.flatpickr-validation')),
    selectPicker = $('.selectpicker');

  // Bootstrap Select
  // --------------------------------------------------------------------
  if (selectPicker.length) {
    selectPicker.selectpicker();
    handleBootstrapSelectEvents();
  }

  // Flat pickr
  if (flatPickrList) {
    flatPickrList.forEach(flatPickr => {
      flatPickr.flatpickr({
        allowInput: true,
        monthSelectorType: 'static'
      });
    });
  }

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const bsValidationForms = document.querySelectorAll('.needs-validation');

  // Loop over them and prevent submission
  Array.prototype.slice.call(bsValidationForms).forEach(function (form) {
    form.addEventListener(
      'submit',
      function (event) {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        } else {
          // Submit your form
          alert('Enviado!!!');
        }

        form.classList.add('was-validated');
      },
      false
    );
  });
})();
/**
 * Form Validation (https://formvalidation.io/guide/examples)
 * ? Primary form validation plugin for this template
 * ? In this example we've try to covered as many form inputs as we can.
 * ? Though If we've miss any 3rd party libraries, then refer: https://formvalidation.io/guide/examples/integrating-with-3rd-party-libraries
 */
//------------------------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    const formValidationExamples = document.getElementById('formValidationExamples'),
      formValidationSelect2Ele = jQuery(formValidationExamples.querySelector('[name="formValidationSelect2"]')),
      formValidationTechEle = jQuery(formValidationExamples.querySelector('[name="formValidationTech"]')),
      formValidationLangEle = formValidationExamples.querySelector('[name="formValidationLang"]'),
      formValidationHobbiesEle = jQuery(formValidationExamples.querySelector('[name="formValidationHobbies"]'));

    const fv = FormValidation.formValidation(formValidationExamples, {
      fields: {
        formValidationName: {
          validators: {
            notEmpty: {
              message: 'Por favor, informe seu nome'
            },
            stringLength: {
              min: 6,
              max: 30,
              message: 'O nome deve possuir entre 6 e 30 caracteres'
            },
            regexp: {
              regexp: /^[a-zA-Z0-9 ]+$/,
              message: 'O nome deve conter apenas letras, números e espaços'
            }
          }
        },
        formValidationEmail: {
          validators: {
            notEmpty: {
              message: 'Por favor, informe seu e-mail'
            },
            emailAddress: {
              message: 'O e-mail informado é inválido'
            }
          }
        },
        formValidationPass: {
          validators: {
            notEmpty: {
              message: 'Por favor, informe sua senha'
            }
          }
        },
        formValidationConfirmPass: {
          validators: {
            notEmpty: {
              message: 'Por favor, confirme sua senha'
            },
            identical: {
              compare: function () {
                return formValidationExamples.querySelector('[name="formValidationPass"]').value;
              },
              message: 'As senhas não coincidem'
            }
          }
        },
        formValidationFile: {
          validators: {
            notEmpty: {
              message: 'Por favor, selecione um arquivo'
            }
          }
        },
        formValidationDob: {
          validators: {
            notEmpty: {
              message: 'Por favor, selecione seu DOB'
            },
            date: {
              format: 'YYYY/MM/DD',
              message: 'A data é inválida'
            }
          }
        },
        formValidationSelect2: {
          validators: {
            notEmpty: {
              message: 'Por favor, informe seu país'
            }
          }
        },
        formValidationLang: {
          validators: {
            notEmpty: {
              message: 'Por favor, informe seu idioma'
            }
          }
        },
        formValidationTech: {
          validators: {
            notEmpty: {
              message: 'Por favor, selecione a tecnologia'
            }
          }
        },
        formValidationHobbies: {
          validators: {
            notEmpty: {
              message: 'Please select your hobbies'
            }
          }
        },
        formValidationBio: {
          validators: {
            notEmpty: {
              message: 'Please enter your bio'
            },
            stringLength: {
              min: 100,
              max: 500,
              message: 'The bio must be more than 100 and less than 500 characters long'
            }
          }
        },
        formValidationGender: {
          validators: {
            notEmpty: {
              message: 'Please select your gender'
            }
          }
        },
        formValidationPlan: {
          validators: {
            notEmpty: {
              message: 'Please select your preferred plan'
            }
          }
        },
        formValidationSwitch: {
          validators: {
            notEmpty: {
              message: 'Please select your preference'
            }
          }
        },
        formValidationCheckbox: {
          validators: {
            notEmpty: {
              message: 'Please confirm our T&C'
            }
          }
        }
      },
      plugins: {
        trigger: new FormValidation.plugins.Trigger(),
        bootstrap5: new FormValidation.plugins.Bootstrap5({
          // Use this for enabling/changing valid/invalid class
          // eleInvalidClass: '',
          eleValidClass: '',
          rowSelector: function (field, ele) {
            // field is the field name & ele is the field element
            switch (field) {
              case 'formValidationName':
              case 'formValidationEmail':
              case 'formValidationPass':
              case 'formValidationConfirmPass':
              case 'formValidationFile':
              case 'formValidationDob':
              case 'formValidationSelect2':
              case 'formValidationLang':
              case 'formValidationTech':
              case 'formValidationHobbies':
              case 'formValidationBio':
              case 'formValidationGender':
                return '.col-md-6';
              case 'formValidationPlan':
                return '.col-xl-3';
              case 'formValidationSwitch':
              case 'formValidationCheckbox':
                return '.col-12';
              default:
                return '.row';
            }
          }
        }),
        submitButton: new FormValidation.plugins.SubmitButton(),
        // Submit the form when all fields are valid
        defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
        autoFocus: new FormValidation.plugins.AutoFocus()
      },
      init: instance => {
        instance.on('plugins.message.placed', function (e) {
          //* Move the error message out of the `input-group` element
          if (e.element.parentElement.classList.contains('input-group')) {
            // `e.field`: The field name
            // `e.messageElement`: The message element
            // `e.element`: The field element
            e.element.parentElement.insertAdjacentElement('afterend', e.messageElement);
          }
          //* Move the error message out of the `row` element for custom-options
          if (e.element.parentElement.parentElement.classList.contains('custom-option')) {
            e.element.closest('.row').insertAdjacentElement('afterend', e.messageElement);
          }
        });
      }
    });

    //? Revalidation third-party libs inputs on change trigger

    // Flatpickr
    const flatpickrDate = document.querySelector('[name="formValidationDob"]');

    if (flatpickrDate) {
      flatpickrDate.flatpickr({
        enableTime: false,
        // See https://flatpickr.js.org/formatting/
        dateFormat: 'Y/m/d',
        // After selecting a date, we need to revalidate the field
        onChange: function () {
          fv.revalidateField('formValidationDob');
        }
      });
    }

    // Select2 (Country)
    if (formValidationSelect2Ele.length) {
      select2Focus(formValidationSelect2Ele);
      formValidationSelect2Ele.wrap('<div class="position-relative"></div>');
      formValidationSelect2Ele
        .select2({
          placeholder: 'Select country',
          dropdownParent: formValidationSelect2Ele.parent()
        })
        .on('change', function () {
          // Revalidate the color field when an option is chosen
          fv.revalidateField('formValidationSelect2');
        });
    }

    // Tagify
    let formValidationLangTagify = new Tagify(formValidationLangEle);
    formValidationLangEle.addEventListener('change', onChange);
    function onChange() {
      fv.revalidateField('formValidationLang');
    }

    //Bootstrap select
    formValidationTechEle.on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
      fv.revalidateField('formValidationTech');
    });
    formValidationHobbiesEle.on('changed.bs.select', function (e, clickedIndex, isSelected, previousValue) {
      fv.revalidateField('formValidationHobbies');
    });
  })();
});
