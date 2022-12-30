console.log("register.js loaded");
const form = document.querySelector("form");
const username = document.querySelector("#username");
const password = document.querySelector("#password");
const email = document.querySelector("#email");
const submit = document.querySelector("#submit");

const url = window.location.hostname;

form.addEventListener("submit",async (e) => {
  e.preventDefault();
  const user = {
    username: username.value,
    password: password.value,
    email: email.value,
  };

  const res = await fetch('/api/users/signup/', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  })
  const data = await res.json()
  const msg = await Swal.fire(
    data.message,
    'Te estamos redireccionando a la página de inicio de sesión',
    'success'
  )

  if (msg.isConfirmed) {
    setTimeout(() => {
      window.location.href = '/login';
    }, 2000)
  }
});
