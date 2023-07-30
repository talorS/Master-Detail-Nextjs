import { Typography, List, ListItem, ListItemText } from '@mui/material';
import parse from 'html-react-parser';
import { getPost } from "@utils/fetchData";

type PostProps = { params: { id: number } }

export default async function Post({ params }: PostProps) {
  const { data: post } = await getPost(params.id);
  const reactElement = parse(post.content);

  return (
    <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
      <ListItem divider>
        <ListItemText
          primary={`Id: ${post.id}`}
          sx={{ color: "black" }}
        />
      </ListItem>
      <ListItem divider>
        <ListItemText
          primary={post.title}
          sx={{ color: "black" }}
        />
      </ListItem>
      <ListItem>
        <Typography
          component="span"
          variant="h6"
          color="text.primary"
        >
          {reactElement}
        </Typography>
      </ListItem>
    </List>
  );
}
