document.addEventListener("DOMContentLoaded", function () {
    const contactForm = document.getElementById('contactForm');
    const contactModal = document.getElementById('contactModal');
    const contactLink = document.getElementById('contactLink');
    const closeModal = document.getElementById('closeModal');

    if (contactForm && contactModal && contactLink && closeModal) {
        contactForm.addEventListener('submit', handleSubmit);
        contactLink.addEventListener('click', handleContactLinkClick);
        closeModal.addEventListener('click', closeContactModal);
    } else {
        console.error('Form Elements not found!');
    }
});

function handleSubmit(event) {
    event.preventDefault();
    const formData = {
        name: document.getElementById('name').value,
        companyName: document.getElementById('companyName').value,
        email: document.getElementById('email').value,
        phoneNumber: document.getElementById('phoneNumber').value,
        message: document.getElementById('message').value,
    };

    fetch("/contact/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': '{{ csrf_token }}'
        },
        body: new URLSearchParams(formData)
    })
        .then(response => response.json())
        .then(data => {
            if (data.status === "success") {
                console.log("Email sent successfully!");
            } else {
                console.error("Error sending email:", data.error);
            }
        });
        closeContactModal();
}

function handleContactLinkClick(event) {
    event.preventDefault();
    if (window.innerWidth <= 768) {
        var menu = document.getElementById('menu');
        if (menu && !menu.classList.contains('invisible')) {
            toggleMenu();
        }
    }
    const contactModal = document.getElementById('contactModal');
    if (contactModal) {
        contactModal.style.opacity = "1";
        contactModal.style.transform = "translateY(0)";
        contactModal.style.pointerEvents = "auto";
    }
}

function closeContactModal() {
    const contactModal = document.getElementById('contactModal');
    if (contactModal) {
        contactModal.style.opacity = "0";
        contactModal.style.transform = "translateY(-100%)";
        setTimeout(() => {
            contactModal.style.pointerEvents = "none";
        }, 700);
    }
}
