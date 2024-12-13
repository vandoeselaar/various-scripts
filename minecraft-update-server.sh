#!/bin/bash

# Paper
latest_version=$(curl -s https://api.papermc.io/v2/projects/paper | jq -r '.versions[-1]')
echo "Checking for new Paper version $latest_version..."

latest_build=$(curl -s "https://api.papermc.io/v2/projects/paper/versions/$latest_version" | jq '.builds[-1]')
curl -s -o paper-latest.jar "https://api.papermc.io/v2/projects/paper/versions/$latest_version/builds/$latest_build/downloads/paper-$latest_version-$latest_build.jar"

if [ -f paper-latest.jar ]; then
    mv paper-latest.jar paper.jar
    echo "Paper updated to version $latest_version build $latest_build."
else
    echo "Failed to download Paper."
fi

# Geyser
echo "Checking for new Geyser version..."
geyser_url="https://download.geysermc.org/v2/projects/geyser/versions/latest/builds/latest/downloads/spigot"
curl -s -L -o geyser-latest.jar "$geyser_url"

if [ -f geyser-latest.jar ]; then
    mv geyser-latest.jar plugins/geyser.jar
    echo "Geyser updated to the latest version."
else
    echo "Failed to download Geyser."
fi

# Floodgate (example URL, if similar format is available)
floodgate_url="https://download.geysermc.org/v2/projects/floodgate/versions/latest/builds/latest/downloads/spigot"
echo "Checking for new Floodgate version..."
curl -s -L -o floodgate-latest.jar "$floodgate_url"

if [ -f floodgate-latest.jar ]; then
    mv floodgate-latest.jar plugins/floodgate.jar
    echo "Floodgate updated to the latest version."
else
    echo "Failed to download Floodgate."
fi

echo "Updates complete!"