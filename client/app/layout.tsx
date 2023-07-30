import "./globals.css";
import Header from "@components/header";
import Footer from "@components/footer";
import Head from './head';

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <Head />
      <body className="bg-gray-900 text-white antialiased">
        <Header />
        <main className="px-4 py-6">{children}</main>
        <Footer />
      </body>
    </html>
  );
}