import { Typography, List, ListItem, ListItemText, Divider } from '@mui/material';
import Link from "next/link";
import { getPostList } from "@utils/fetchData";
import React from 'react';
import parse from 'html-react-parser';

const activeStyle: string = 'hover:underline hover:bg-amber-300';

export default async function ListOfPosts() {
  const { data: posts } = await getPostList();

  return (
    <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
      {posts.map(item => {
        const reactElement = parse(item.content);
        return <React.Fragment key={item.id}>
          <ListItem alignItems="flex-start" sx={{
            display: 'flex',
            flexDirection: 'column',
            justifyContent: 'flex-start'
          }}>
            <ListItemText
              primary={<Link href={`/posts/${item.id}`} className={activeStyle}>
                {item.title}
              </Link>}
              sx={{ color: "black" }}
            />
            <Typography
              component="span"
              variant="h6"
              color="text.primary"
            >
              {reactElement}
            </Typography>
          </ListItem>
          <Divider variant="fullWidth" component="li" />
        </React.Fragment>
      })}
    </List>
  );
}
