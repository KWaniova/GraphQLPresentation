import { useQuery, gql } from "@apollo/client";
import MissionsList from "./components/missions_list";

const FILMS_QUERY = gql`
  {
    launchesPast(limit: 10) {
      id
      mission_name
    }
  }
`;

export default function App() {
  const { data, loading, error } = useQuery(FILMS_QUERY);

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
      <h1 style={{ fontFamily: "arial" }}>SpaceX Launches</h1>
      <ul style={{ fontFamily: "arial" }}>
        {data.launchesPast.map(
          (launch: { id: string; mission_name: string }) => (
            <li style={{ padding: 5 }} key={launch.id}>
              {launch.mission_name}
            </li>
          )
        )}
      </ul>
      <div style={{ margin: 5 }}>
        <MissionsList />
      </div>
    </div>
  );
}
