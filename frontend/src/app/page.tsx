"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    fetch("/api/backend-message")
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return res.json();
      })
      .then((data) => setMessage(data.message ?? "No message returned"))
      .catch(() => setMessage("Unable to reach backend"));
  }, []);

  return (
    <main className="p-10">
      <h1 className="text-3xl font-bold">
        DSA Duel
      </h1>

      <p className="mt-4">
        Backend says: {message}
      </p>
    </main>
  );
}
