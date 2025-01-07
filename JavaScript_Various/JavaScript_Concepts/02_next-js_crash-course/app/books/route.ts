import books from "../api/db";

export async function GET() {
    return Response.json(books);
}