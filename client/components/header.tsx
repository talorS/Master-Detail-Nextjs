import { Divider } from "@mui/material";
import NavLink from "./nav-link";

export default function Header() {
  return (
    <header className="p-4 border-b border-gray-800 flex justify-between items-center text-sm font-semibold">
      <div className="space-x-6 flex items-center">
        <NavLink
          activeClassName="text-white"
          inactiveClassName="text-gray-400 hover:text-white"
          href="/"
        >
          Home
        </NavLink>
        <NavLink
          activeClassName="text-white"
          inactiveClassName="text-gray-400 hover:text-white"
          href="/posts"
        >
          Posts
        </NavLink>
      </div>
    </header>
  );
}