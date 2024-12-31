import React, { useState } from 'react';

function BookCall() {
    const [formData, setFormData] = useState({ name: '', email: '', topic: '' });

    const handleChange = e => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleSubmit = e => {
        e.preventDefault();
        fetch('http://127.0.0.1:5000/book-call', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData),
        })
            .then(res => {
                if (!res.ok) {
                    throw new Error(`HTTP error! status: ${res.status}`);
                }
                return res.json();
            })
            .then(data => alert(data.message))
            .catch(err => console.error(err));
         };

    return (
        <div className="book-call">
        <h1>Book a Call</h1>
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                name="name"
                placeholder="Name"
                value={formData.name}
                onChange={handleChange}
                required
            />
            <input
                type="email"
                name="email"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
                required
            />
            <textarea
                name="topic"
                placeholder="Topic"
                value={formData.topic}
                onChange={handleChange}
                required
            ></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>
    );
}

export default BookCall;
