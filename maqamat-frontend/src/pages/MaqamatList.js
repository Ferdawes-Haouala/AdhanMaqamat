import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

function MaqamatList() {
    const [maqamat, setMaqamat] = useState([]);
    
    useEffect(() => {
    fetch('/maqamat')
    .then(res => res.json())
    .then(data => setMaqamat(data))
    .catch(err => console.error(err));
    }, []);
    return (
    <div className="maqamat-list">
        <h1>Maqamat</h1>
        <ul>
        {maqamat.map(maqam => (
            <li key={maqam.id}>
                <Link to={`/maqamat/${maqam.id}`}>{maqam.name}</Link>
            </li>
        ))}
        </ul>
    </div>
    );
}

export default MaqamatList;
