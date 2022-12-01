import { useQuery, gql } from "@apollo/client";

const BOOKS_QUERY = gql`
  {
    books {
      id
      title
    }
  }
`;

export default function App() {
  const { data, loading, error } = useQuery(BOOKS_QUERY);

  if (loading) return <>Loading...</>;
  if (error) return <pre>{error.message}</pre>;

  return (
    <div
      style={{
        width: "100vw",
        height: "100vh",
        display: "flex",
        alignItems: "center",
        flexDirection: "column",
        overflow: "scroll",
      }}
    >
      <h1 style={{ fontFamily: "arial" }}>Books</h1>
      <ul style={{ fontFamily: "arial" }}>
        {data.books.map((book: { id: string; title: string }) => (
          <li style={{ padding: 5 }} key={book.id}>
            {book.title}
          </li>
        ))}
      </ul>
      {/* <div style={{ margin: 5 }}>
        <MissionsList />
      </div> */}
    </div>
  );
}
