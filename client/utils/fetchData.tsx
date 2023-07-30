const API_URL: string = 'http://localhost:8080/api';

type BASE_RESPONSE = {
  res: string
}

type HP_DATA_RESPONSE = BASE_RESPONSE & {
  data: {
    headline: string
  }
}

type POSTS_RESPONSE = BASE_RESPONSE & {
  data: Post[]
}

type POST_RESPONSE = BASE_RESPONSE & {
  data: Post
}

type Post = {
  id: number,
  title: string;
  content: string
}


export const getHpData = async (): Promise<HP_DATA_RESPONSE> => {
  const res = await fetch(`${API_URL}/get_hp_data`);
  return res.json();
}

export const getPostList = async (): Promise<POSTS_RESPONSE> => {
  let res = await fetch(`${API_URL}/get_posts`);
  return res.json();
};

export const getPost = async (id: number): Promise<POST_RESPONSE> => {
  let res = await fetch(`${API_URL}/get_post/${id}`);
  return res.json();
};