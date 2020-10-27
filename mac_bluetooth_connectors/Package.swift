// swift-tools-version:4.2
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "bt-connect",
    dependencies: [
        // Dependencies declare other packages that this package depends on.
        .package(url: "https://github.com/lapfelix/SimpleCLI.git", from: "0.1.0"),
    ],
    targets: [
        // Targets are the basic building blocks of a package. A target can define a module or a test suite.
        // Targets can depend on other targets in this package, and on products in packages which this package depends on.
        .target(
            name: "bt-connect",
            dependencies: ["SimpleCLI"]),
        .testTarget(
            name: "bt-connectTests",
            dependencies: ["bt-connect"]),
    ]
)
