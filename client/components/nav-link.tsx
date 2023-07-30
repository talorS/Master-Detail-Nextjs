"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";

export default function NavLink({
  activeClassName,
  inactiveClassName,
  children,
  href,
  ...rest
}: any) {
  const pathname = usePathname();

  const classes =
    pathname === href
      ? `${activeClassName}`
      : `${inactiveClassName}`;

  return (
    <Link href={href} className={classes} {...rest}>
      {children}
    </Link>
  );
}