import { NextResponse } from "next/server";

const BACKEND_INTERNAL_URL = process.env.BACKEND_INTERNAL_URL ?? "http://backend:8000";

export async function GET() {
  try {
    const response = await fetch(`${BACKEND_INTERNAL_URL}/`, {
      cache: "no-store",
    });

    if (!response.ok) {
      return NextResponse.json(
        { message: `Backend unavailable (HTTP ${response.status})` },
        { status: 502 },
      );
    }

    const data = await response.json();
    return NextResponse.json(data);
  } catch {
    return NextResponse.json(
      { message: "Unable to reach backend" },
      { status: 502 },
    );
  }
}
