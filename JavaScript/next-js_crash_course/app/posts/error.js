// Error handling. Whenever some error occurs, this code is going to automatically run. 

'use client'; // Error components must be Client components. 

import { useEffect } from "react";

const Error = ({error, reset}) => {
    useEffect(() => {
        // Log the error to an error reporting service. 
        console.log(error);
    }, [error]);

    return (
        <div>
            <h2>
                <button
                    onC
                />
            </h2>
        </div>
    )
}
