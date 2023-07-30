import { Divider, Typography } from "@mui/material";
import React from "react";

export default function Footer() {
    return (
        <React.Fragment>
            <footer>
                <Divider variant="fullWidth" sx={{ backgroundColor: "white" }} />
                <Typography
                    component="span"
                    variant="body2"
                    color="white"
                >
                    Footer Section
                </Typography>
            </footer>
        </React.Fragment>
    );
}