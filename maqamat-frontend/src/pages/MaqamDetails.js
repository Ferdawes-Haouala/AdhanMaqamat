import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

function MaqamDetails() {
    const { id } = useParams();
    const [maqam, setMaqam] = useState(null);

    useEffect(() => {
    fetch(`/maqamat/${id}`) // Adjust to your backend endpoint
        .then(res => res.json())
        .then(data => setMaqam(data))
        .catch(err => console.error(err));
    }, [id]);

    if (!maqam) return <p>Loading...</p>;

    return (
    <div className="maqam-details">
        <h1>{maqam.name}</h1>
        <p>{maqam.description}</p>
        <ul>
            {maqam.links.map((link, index) => (
            <li key={index}>
                <a href={link} target="_blank" rel="noopener noreferrer">{link}</a>
            </li>
        ))}
        </ul>
    </div>
);
}

export default MaqamDetails;
