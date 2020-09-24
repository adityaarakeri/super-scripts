import XCTest

#if !os(macOS)
public func allTests() -> [XCTestCaseEntry] {
    return [
        testCase(bt_connectTests.allTests),
    ]
}
#endif