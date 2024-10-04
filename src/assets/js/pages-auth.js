/**
 *  Pages Authentication
 */

'use strict';
const formAuthentication = document.querySelector('#formAuthentication');
const btnSubmit = document.getElementById('btnSubmit');
const btnText = document.getElementById('btnText');
const btnLoader = document.getElementById('btnLoader');
const numeralMask = document.querySelectorAll('.numeral-mask');

document.addEventListener('DOMContentLoaded', function (e) {
  (function () {
    // Validate the form using FormValidation library
    if (formAuthentication) {
      const fv = FormValidation.formValidation(formAuthentication, {
        fields: {
          username: {
            validators: {
              notEmpty: {
                message: 'Informe o nome de usuário'
              },
              stringLength: {
                min: 4,
                message: 'Nome de usuário deve ter mais de 4 caracteres'
              }
            }
          },
          email: {
            validators: {
              notEmpty: {
                message: 'Informe seu e-mail'
              },
              emailAddress: {
                message: 'Informe um endereço de e-mail válido'
              }
            }
          },
          'email-username': {
            validators: {
              notEmpty: {
                message: 'Informe o e-mail ou nome de usuário'
              },
              stringLength: {
                min: 4,
                message: 'Nome de usuário deve ter mais de 4 caracteres'
              }
            }
          },
          password: {
            validators: {
              notEmpty: {
                message: 'Informe sua senha'
              },
              stringLength: {
                min: 4,
                message: 'Senha deve ter mais de 4 caracteres'
              }
            }
          },
          'confirm-password': {
            validators: {
              notEmpty: {
                message: 'Confirme a senha'
              },
              identical: {
                compare: function () {
                  return formAuthentication.querySelector('[name="password"]').value;
                },
                message: 'A senha e sua confirmação são diferentes'
              },
              stringLength: {
                min: 4,
                message: 'Senha deve ter mais de 4 caracteres'
              }
            }
          },
          terms: {
            validators: {
              notEmpty: {
                message: 'Aceite os termos e condições'
              }
            }
          }
        },
        plugins: {
          trigger: new FormValidation.plugins.Trigger(),
          bootstrap5: new FormValidation.plugins.Bootstrap5({
            eleValidClass: '',
            rowSelector: '.mb-5'
          }),
          submitButton: new FormValidation.plugins.SubmitButton(),

          defaultSubmit: new FormValidation.plugins.DefaultSubmit(),
          autoFocus: new FormValidation.plugins.AutoFocus()
        },
        init: instance => {
          instance.on('plugins.message.placed', function (e) {
            if (e.element.parentElement.classList.contains('input-group')) {
              e.element.parentElement.insertAdjacentElement('afterend', e.messageElement);
            }
          });
        }
      });

      if (btnSubmit && btnText && btnLoader) {
        // Show loading state on form submission
        btnSubmit.addEventListener('click', function (event) {
          event.preventDefault(); // Prevent default form submission

          // Check if the form is valid
          fv.validate().then(function (status) {
            if (status === 'Valid') {
              // If the form is valid, show loading state
              btnSubmit.classList.add('disabled');
              btnText.textContent = 'Enviando e-mail... ';
              btnLoader.classList.remove('visually-hidden');
            }
          });
        });
      }
    }

    // Verification masking
    if (numeralMask.length) {
      numeralMask.forEach(e => {
        new Cleave(e, {
          numeral: true
        });
      });
    }
  })();
});
