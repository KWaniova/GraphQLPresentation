import { useQuery, gql } from "@apollo/client";

interface Mission {
  id: number;
  description: string;
  name: string;
  wikipedia: string;
}

interface MissionsData {
  missions: Mission[];
}

interface MisionsQuery {
  find?: {
    id?: string;
    name?: string;
  };
  limit?: number;
}

const GET_MISSIONS = gql`
  query GetMissions($limit: Int) {
    missions(limit: $limit) {
      id
      description
      name
      wikipedia
    }
  }
`;

export default function MisionsList() {
  const { loading, data } = useQuery<MissionsData, MisionsQuery>(GET_MISSIONS, {
    variables: {
      limit: 10,
    },
  });
  return (
    <div style={{ fontFamily: "arial" }}>
      <h3>Missions</h3>
      {loading ? (
        <p>Loading ...</p>
      ) : (
        <div style={{ display: "flex", flexDirection: "column" }}>
          {data &&
            data.missions.map((mission) => (
              <div
                style={{
                  border: "1px solid gray",
                  margin: 5,
                  padding: 10,
                  borderRadius: 10,
                }}
              >
                <div style={{ paddingBottom: 10 }}>
                  <div>
                    <b>ID:</b> {mission.id}
                  </div>
                  <div>
                    <b>NAME: </b>
                    {mission.name}
                  </div>
                </div>
                <div>{mission.description}</div>
              </div>
            ))}
        </div>
      )}
    </div>
  );
}
