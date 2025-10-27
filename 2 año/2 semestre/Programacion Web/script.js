document.addEventListener('DOMContentLoaded', function() {

    //Boton volver arriba
    const botonVolver = document.getElementById('volverArriba');
    
    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 300) {
            botonVolver.classList.add('mostrar');
        } else {
            botonVolver.classList.remove('mostrar');
        }
    });
    
    botonVolver.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    //Validacion del formulario
    document.querySelector('form').addEventListener('submit', (e) => {
        e.preventDefault();
        
        // Limpiar errores
        document.querySelectorAll('.mensaje-error').forEach(el => el.remove());
        document.querySelectorAll('.campo-error').forEach(el => el.classList.remove('campo-error'));
        
        const campos = ['nombre', 'email', 'mensaje'].map(name => 
            document.querySelector(`[name="${name}"]`)
        );
        
        let valido = true;
        
        campos.forEach((campo, i) => {
            const valor = campo.value.trim();
            if (!valor) {
                mostrarError(campo, ['El nombre', 'El email', 'El mensaje'][i] + ' es obligatorio');
                valido = false;
            } else if (i === 1 && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(valor)) {
                mostrarError(campo, 'Ingresa un email válido');
                valido = false;
            }
        });
        
        if (valido) {
            console.log('Formulario enviado correctamente');
            guardarDatosFormulario();
            e.reset();
        }
    });
    
    function mostrarError(campo, mensaje) {
        campo.classList.add('campo-error');
        campo.insertAdjacentHTML('afterend', `<div class="mensaje-error">${mensaje}</div>`);
    }


    //Boton Expansion Proyectos 
    document.querySelectorAll('.proyecto-checkbox').forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const id = this.id.replace('Abrir', 'Contenido');
            const contenido = document.getElementById(id);
            const label = document.querySelector(`label[for="${this.id}"]`);
            
            if (this.checked) {
                contenido.classList.add('mostrar');
                label.innerHTML = `<i class="fi fi-br-angle-up"></i>`;
            } else {
                contenido.classList.remove('mostrar');
                label.innerHTML = `<i class="fi fi-br-angle-down"></i>`;
            }
        });
    });


    // Mostrar fecha actual en el pie de página
    const ahora = new Date();
    const fecha = ahora.toLocaleDateString('es-ES', {
        day: '2-digit',
        month: '2-digit', 
        year: 'numeric'
    });
    
    const footer = document.querySelector('footer p');
    footer.innerHTML = `Contacto - Mail: angelesleguiza28@gmail.com - Teléfono: 2646730695 - ${fecha} - ©2025 Leguiza Angeles`;


    
    //Guardar datos del formulario en localStorage
    function guardarDatosFormulario() {
        const datosFormulario = {
            nombre: document.querySelector('input[name="nombre"]').value,
            email: document.querySelector('input[name="email"]').value,
            mensaje: document.querySelector('textarea[name="mensaje"]').value
        };
        
        localStorage.setItem('formularioContacto', JSON.stringify(datosFormulario));
        console.log('Datos guardados correctamente');
    }


    //Boton tema Claro/Oscuro
    const Checkbox = document.getElementById("Checkbox");
    const Icono = document.getElementById("Tema")

    Checkbox.addEventListener('change', function() {
        if (this.checked) {
            document.documentElement.setAttribute('Tema', 'Oscuro');
            Icono.innerHTML = `<i class="fi fi-br-sun"></i>`;
        }else{
            document.documentElement.removeAttribute('Tema');
            Icono.innerHTML = `<i class="fi fi-br-moon"></i>`;
        }
    })

});