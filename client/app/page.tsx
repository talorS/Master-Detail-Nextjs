import parse from 'html-react-parser';
import { getHpData } from "@utils/fetchData";
import Box from '@mui/material/Box';

export default async function Home() {
  const { data: { headline } } = await getHpData();
  const reactElement = parse(headline);
  return (
    <Box sx={{ p: 2, border: '1px dashed grey', width: 'min-content' }}>
      {reactElement}
    </Box>
  );
}