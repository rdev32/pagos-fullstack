console.log("login.js loaded");
const form = document.querySelector("form");
const email = document.querySelector("#email");
const password = document.querySelector("#password");
const save = document.querySelector("#save_login");

const url = window.location.hostname;

form.addEventListener("submit",async (e) => {
  e.preventDefault();
  const user = {
    email: email.value,
    password: password.value,
  };

  const req = await fetch('/api/users/login/', {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(user),
  })
  const res = await req.json()
  if (res.status === false) {
      const msg = await Swal.fire({
      icon: 'error',
      title: res.message,
      text: 'Esas credenciales no son correctas',
    })
    if (msg.isConfirmed) {
      setTimeout(() => {
        window.location.href = '/login';
      }, 2000)
    }
  } else {
    const { data } = res
    window.localStorage.setItem("token", data.tokens.access);
    window.localStorage.setItem("refresh", data.tokens.refresh);
    window.localStorage.setItem("id", data.tokens.refresh);
    const msg = await Swal.fire(
      res.message,
      'Te estamos redireccionando a la página de inicio de sesión',
      'success'
    )
    if (msg.isConfirmed) {
      setTimeout(() => {
        window.location.href = '/dashboard';
      }, 2000)
    }
  }
})